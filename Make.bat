@echo off
setlocal enabledelayedexpansion

REM Définition des variables
set ANGULAR_IMAGE=angular-enviedici-app:latest
set DJANGO_IMAGE=django-enviedici-app:latest
set ANGULAR_PATH=angular-app
set DJANGO_PATH=django_backend
set DJANGO_ENV_FILE=%DJANGO_PATH%\.env

REM Récupération de la commande passée
set CMD=%1

if "%CMD%"=="" (
    set CMD=up
)

if "%CMD%"=="build-angular" (
    echo 🔧 Build de l'application Angular...
    docker build -t %ANGULAR_IMAGE% %ANGULAR_PATH%
    exit /b
)

if "%CMD%"=="build-django" (
    echo 🔧 Build de l'application Django...
    docker build -t %DJANGO_IMAGE% %DJANGO_PATH%
    exit /b
)

if "%CMD%"=="angular" (
    echo 🚀 Lancement d'Angular sur http://localhost:4200
    docker run -d --rm -p 4200:80 --name angular %ANGULAR_IMAGE%
    exit /b
)

if "%CMD%"=="django" (
    echo 🚀 Lancement de Django sur http://localhost:8000
    docker run -d --rm -p 8000:8000 --env-file %DJANGO_ENV_FILE% --name django %DJANGO_IMAGE%
    exit /b
)

if "%CMD%"=="up" (
    call %~f0 build-angular
    call %~f0 build-django
    call %~f0 angular
    call %~f0 django
    exit /b
)

if "%CMD%"=="restart" (
    echo 🛑 Arrêt des conteneurs...
    docker stop angular >nul 2>&1
    docker stop django >nul 2>&1
    echo 🚀 Redémarrage des conteneurs...
    call %~f0 build-angular
    call %~f0 build-django
    call %~f0 angular
    call %~f0 django
    exit /b
)

if "%CMD%"=="down" (
    echo 🛑 Arrêt des conteneurs...
    docker stop angular >nul 2>&1
    docker stop django >nul 2>&1
    exit /b
)

if "%CMD%"=="clean" (
    call %~f0 down
    echo 🧹 Suppression des images...
    docker rmi %ANGULAR_IMAGE% -f >nul 2>&1
    docker rmi %DJANGO_IMAGE% -f >nul 2>&1
    exit /b
)

echo ❓ Commande inconnue : %CMD%
echo Commandes valides : up, down, clean, angular, django, build-angular, build-django
exit /b
