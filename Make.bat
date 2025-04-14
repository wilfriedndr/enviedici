@echo off
setlocal enabledelayedexpansion

REM === Définition des variables ===
set ANGULAR_IMAGE=angular-enviedici-app:latest
set DJANGO_IMAGE=django-enviedici-app:latest
set POSTGRES_IMAGE=postgres-enviedici:latest

set ANGULAR_PATH=angular-app
set DJANGO_PATH=django_backend
set POSTGRES_PATH=postgres
set DJANGO_ENV_FILE=%DJANGO_PATH%\.env

set NETWORK_NAME=enviedici-net

REM === Commande passée ===
set CMD=%1
if "%CMD%"=="" set CMD=up

REM === Création du réseau si inexistant ===
docker network inspect %NETWORK_NAME% >nul 2>&1
if errorlevel 1 (
    echo Création du réseau Docker %NETWORK_NAME%...
    docker network create %NETWORK_NAME%
)

REM === Build ===
if "%CMD%"=="build-angular" (
    echo Build de l'application Angular...
    docker build -t %ANGULAR_IMAGE% %ANGULAR_PATH%
    exit /b
)

if "%CMD%"=="build-django" (
    echo Build de l'application Django...
    docker build -t %DJANGO_IMAGE% %DJANGO_PATH%
    exit /b
)

if "%CMD%"=="build-postgres" (
    echo Build de l'image PostgreSQL...
    docker build -t %POSTGRES_IMAGE% %POSTGRES_PATH%
    exit /b
)

REM === Lancement des conteneurs ===
if "%CMD%"=="angular" (
    echo Lancement d'Angular sur http://localhost:4200/app/
    docker run -d --rm --name angular --network %NETWORK_NAME% -p 4200:80 %ANGULAR_IMAGE%
    exit /b
)

if "%CMD%"=="postgres" (
    echo Lancement de PostgreSQL sur le port 5432...
    docker run -d --rm --name postgres --network %NETWORK_NAME% ^
        -e POSTGRES_DB=enviedici ^
        -e POSTGRES_USER=enviedici ^
        -e POSTGRES_PASSWORD=enviedici ^
        -v postgres-data:/var/lib/postgresql/data ^
        -p 5432:5432 ^
        %POSTGRES_IMAGE%
    exit /b
)

if "%CMD%"=="django" (
    echo Lancement de Django sur http://localhost:8000/api/
    docker run -d --rm --name django --network %NETWORK_NAME% ^
        --env-file %DJANGO_ENV_FILE% ^
        -p 8000:8000 ^
        %DJANGO_IMAGE%
    exit /b
)

REM === Version debug Django sans --rm pour voir les logs ===
if "%CMD%"=="django-debug" (
    echo [DEBUG] Lancement de Django DEBUG sans option --rm pour voir les logs
    docker run -it --name django-debug --network %NETWORK_NAME% ^
        --env-file %DJANGO_ENV_FILE% ^
        -p 8000:8000 ^
        %DJANGO_IMAGE%
    exit /b
)

REM === Démarrage complet ===
if "%CMD%"=="up" (
    call %~f0 build-angular
    call %~f0 build-django
    call %~f0 build-postgres
    timeout /t 3 >nul
    call %~f0 postgres
    timeout /t 3 >nul
    call %~f0 angular
    timeout /t 3 >nul
    call %~f0 django
    exit /b
)

REM === Nettoyage ===
if "%CMD%"=="down" (
    echo Arrêt des conteneurs...
    docker stop angular >nul 2>&1
    docker stop django >nul 2>&1
    docker stop postgres >nul 2>&1
    docker stop django-debug >nul 2>&1
    exit /b
)

if "%CMD%"=="clean" (
    call %~f0 down
    echo Suppression des images...
    docker rmi %ANGULAR_IMAGE% -f >nul 2>&1
    docker rmi %DJANGO_IMAGE% -f >nul 2>&1
    docker rmi %POSTGRES_IMAGE% -f >nul 2>&1
    exit /b
)

if "%CMD%"=="restart" (
    call %~f0 clean
    call %~f0 up
    exit /b
)

REM === Commande inconnue ===
echo Commande inconnue : %CMD%
echo Commandes disponibles :
echo      up, down, clean, restart
echo      angular, django, django-debug, postgres
echo      build-angular, build-django, build-postgres
exit /b
