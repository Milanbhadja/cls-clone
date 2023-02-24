Image CLassification:

This repo contain thre categories.

Setting up the Environment

python3 -m pip install -U virtualenv # install the virtualenv
virtualenv -p python3 dev_env # creating an environment
source dev_env/bin/activate # activate environment
git clone https://github.com/entiretydotai/Image-Classification-and-Deployment #clone the repo
cd Image-Classification-and-Deployment
pip install -r requirements.txt # install the requirements
Deep learning model: For classification, transfer learning techniques has been used as it has preweights. I also some of the layer on top of that. Once it has been trained, I have save model so we can directly use on other dataset.

Now we have to make API so we can predict label according to that. we will use flask for creating web app.

Flask

Flask is great for developers working on small projects that need a quick way to make a simple, Python-powered web site. It powers loads of small one-off tools, or simple web interfaces built over existing APIs.

let's take an example of flask:

from flask import Flask ''' app = Flask(name)

@app.route("/") def hello_world(): return "

Hello, World!

"
'''

In gui of webapp, user can upload image as a output they got to know that image is from which category.

UPLOAD IMAGES

![upload image](https://github.com/Milanbhadja/classification/blob/main/static/upload_image.png)

Prediction

![predicted result](https://github.com/Milanbhadja/classification/blob/main/static/prediction%20image.png)

Craete new virtual enviornment to install all dependencies.

python -m venv ./venv
dir ./venv
cd venv\Scripts
activate
After that install all libraries: pip install -r requirement.txt

After that all app has been dockerised with docker.

Docker

Docker is a platform that allows users to easily pack, distribute, and manage applications within containers. It's an open-source project that automates the deployment of applications inside software containers. Gone are the days of an IT professional saying "Well, it worked on my machine." Not it works on all of our machines.

Heroku:

Heroku integrates with GitHub to make it easy to deploy code living on GitHub to apps running on Heroku. When GitHub integration is configured for a Heroku app, Heroku can automatically build and release (if the build is successful) pushes to the specified GitHub repo.

Once it has been contenerised, create CI/CD pipeline for github action.

I have Heroku free version which allows only 500 mb to upload your model. Unfortunately, our model size is more than 500MB so we couldn't attach CI/CD pipeline.

![Heroku image ](https://github.com/Milanbhadja/classification/blob/main/static/Heroku%20Error.png)

I will try to implement CI/CD pipeline with different yaml file. I will upload it soon.