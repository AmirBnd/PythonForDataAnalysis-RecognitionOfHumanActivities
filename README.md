# Analyse du DataSet suivant (Smartphone Based Recognition Of Human Activities And Postural Transitions) : 
https://archive.ics.uci.edu/ml/datasets/Smartphone-Based+Recognition+of+Human+Activities+and+Postural+Transitions

#### Travail Réalisé par : Amir BENADOUDA
#### Contexte : Dans le cadre d'une étude (ESILV)
#### Contact : amir.benadouda@edu.devinci.fr

## Introduction

30 participants ont effectués des activités de la vie quotidienne tout en portant un smartphone à leur ceinture. Grâce à la centrale inertielle dont le smartphone est équipé, il fut possible de configurer ce dernier pour enregistrer les mouvements de ces personnes, et notamment leurs positions (allongé, debout, assis, etc.). Ainsi, les données prdouites nous proviennent de deux capteurs : Un accéléromètre et un gyroscope.
#### Le jeu de données à, de ce fait, pu être partitionné de façon aléatoire et intrasèque. Par la suite, nous retrouverons une selection de 70% des volontaires afin de générer le dataset d'entrainement ("Train"); ainsi que les 30% retant qui serviront à générer le dataset de test ("Test").

## Accès à l'ensemble de l'étude
##### Si vous souhaitez acceder et visualiser toute l'étude et l'analyse qui a été réalisée, je vous invite à consulter le fichier suivant : "Etude du DataSet (NoteBook).ipynb"

## Lancement des scripts et test des modèles
##### Pour lancer tout le code, et tester les différents modèles mis en place lors de l'analyse du DataSet que j'ai pu réaliser, il vous faut d'abord les prérequis suivant : 

1 - Installer Python : https://www.python.org/downloads/<br/>
2 - Installer Anaconda : ttps://www.anaconda.com/distribution/#download-section<br/>
3 - Ouvrir Anaconda Powershell Prompt (Clique droit puis "executer en tant qu'administrateur")<br/>
4 - Installer les packages suivants en tappant les lignes de code ci-dessous<br/><br/>
    pip install pandas<br/>
    pip install numpy<br/>
    pip install matplotlib<br/>
    pip install seaborn<br/>
    pip install plotly<br/>
    pip install cycler<br/>
    pip install scipy<br/>
    pip install sklearn<br/>
    pip install keras<br/>
    pip install lightgbm<br/>
    pip install django<br/><br/>
5 - Ouvir votre shell et faire un "git clone https://github.com/oOMiRoUOo/PythonForDataAnalysis-RecognitionOfHumanActivities.git" dans le dossier de votre choix, ou directement télécharger le .zip depuis Github et décompresserle dossier.<br/>
6 - Ouvrir "Jupyter Notebook (Anaconda)"<br/>
7 - Ouvrir le fichier "Etude du DataSet (NoteBook).ipynb"<br/>
8 - Executez tous les scripts<br/>

## Lancer l'API
#### Ouvrez Anaconda Powershell Prompt, placez vous dans le dossier API. Faites un "python manage.pyrunserver".

## Résumé
#### Un résumé de l'étude est disponible sous forme de powerpoint sur le fichier "Présentation.pptx".
