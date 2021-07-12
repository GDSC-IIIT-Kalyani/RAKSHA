<!-- PROJECT SHIELDS -->
<!--
*** Using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="static/logo.PNG" alt="Logo" width="350" height="350">

  <h3 align="center">RAKSHA</h3>

  <p align="center">
    Virtual Self Defense Trainer
    <br />
    <br />
    ·
    <a href="https://drive.google.com/file/d/1zXvHk6HpLrv-2i127cx1vv41eDuQ-IVt/view?usp=sharing">Video link</a>
    ·
    <a href="https://github.com/akshitadixit/RAKSHA/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/akshitadixit/RAKSHA/issues/new">Request Feature</a>
    ·
  </p>
</p>


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- ABOUT THE PROJECT -->
## About The Project

Self-defence is an important skill for self safety especially for women in times of danger. However, self-defence training is not accessible to many. And specially in these times when you cannot take one-on-one training due to lockdown restrictions, Techquillas present here your virtual self defense trainer RAKSHA which not only guides you with 11 basic self defense techniques but also grades you on how accurately you perform. Keep practicing, keep earning points and move on to the next modules! We walk you through by also taking some self awareness quizzes that help you stay on top of the leaderboard.

The team presents a framework that estimates human pose using a webcam and mediapipe and analyzes the pose in order to give a score and performance based review. This framework aims at teaching self defense to users. Then features are extracted and the poses aligned in the temporal domain. The result of the overall pipeline is a score and model.predict for each feature extracted.


### Built With

We build our backend using the following technologies:
* Flask
* Firebase
* Mediapipe
* Tensorflow
* Keras
* OpenCV

The frontend involves basic web development using Bootstrap, HTML, CSS and JavaScript.


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may set up the project locally.
To get a local copy up and running follow these simple example steps.


Assuming you have Ananconda or Miniconda3 already working, create a tensorflow conda environment and install a few libraries into it, and then we're ready to go.

* Install the current release of CPU-only TensorFlow, recommended for beginners:

```bash
conda create -n tf tensorflow
conda activate tf
```

* Or, to install the current release of GPU TensorFlow on Linux or Windows:

```bash
conda create -n tf-gpu tensorflow-gpu
conda activate tf-gpu
```

* Cd into your newly created environment (from command line or terminal)
```bash
cd C:\...\path-to-your-conda-environment\
```

* Installing modules we will need 
Though your virtual env will have all required modules, here are some extra ones required to setup this project locally.
```bash
pip install -r requirements.txt
```

## Running the code

* Fork and clone the project.

```bash
git clone https://github.com/akshitadixit/RAKSHA
```
* Cd into your cloned repo (folder with the same name as the repo on your system)
```bash
cd C:\...\path-to-your-cloned-repo\
```
* After making sure your tf conda environment we just created above, is activated, run the app.py file
```bash
python app.py
```

Succesfull installation and running will give you a link you can visit locally. For any exceptions, kindly recheck the entire process and try again, or feel free to create an issue.

### Dependencies
For the complete list visit [requirements.txt](https://github.com/akshitadixit/RAKSHA/blob/master/requirements.txt)


<!-- USAGE EXAMPLES -->
## Screenshots
![land](https://user-images.githubusercontent.com/72789934/125187061-5ca9f980-e24b-11eb-991e-9504b4789acc.PNG)
![reg](https://user-images.githubusercontent.com/72789934/125187162-d7731480-e24b-11eb-9a4a-ec4cc1c14ac2.PNG)
![Screenshot from 2021-07-11 12-27-58](https://user-images.githubusercontent.com/56997545/125187699-87498180-e24e-11eb-8edc-9b2372b3bfa6.png)



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/akshitadixit/RAKSHA) for a list of proposed features (and known issues).

## VIDEOS
Video link - https://drive.google.com/file/d/1zXvHk6HpLrv-2i127cx1vv41eDuQ-IVt/view?usp=sharing


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- ACKNOWLEDGEMENTS -->
## Our Contributors👩‍💻👨‍💻 :
<a href="https://github.com/akshitadixit/RAKSHA/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=akshitadixit/RAKSHA" />
</a>

<a href="https://github.com/akshitadixit/RAKSHA/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=akshitadixit/RAKSHA">
</a>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/akshitadixit/RAKSHA.svg?style=plastic
[contributors-url]: https://github.com/akshitadixit/RAKSHA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/akshitadixit/RAKSHA.svg?style=plastic
[forks-url]: https://github.com/akshitadixit/RAKSHA/network/members
[stars-shield]: https://img.shields.io/github/stars/akshitadixit/RAKSHA.svg?style=plastic
[stars-url]: https://github.com/akshitadixit/RAKSHA/stargazers
[issues-shield]: https://img.shields.io/github/issues/akshitadixit/RAKSHA.svg?style=plastic
[issues-url]: https://github.com/akshitadixit/RAKSHA/issues
[license-shield]: https://img.shields.io/github/license/akshitadixit/RAKSHA.svg?style=plastic
[license-url]: https://github.com/akshitadixit/RAKSHA/blob/master/LICENSE.txt
