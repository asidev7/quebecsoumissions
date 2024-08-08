# Utiliser l'image officielle de Python comme image de base
FROM python:3.11

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le fichier .env dans le conteneur
COPY .env /app/

# Copier le reste du code de l'application dans le répertoire de travail
COPY . /app/

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour démarrer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
