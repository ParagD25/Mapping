# Mountain and Volcano Mapping 🗺️:
Creating map using Folium library and pinning the locations of major volcanoes and mountains <br>
Data of all the mountains and volcanoes are  in  `mountain.txt` and `volcano.txt` respectively. <br>
Popup icon specifies weather it is a <b>mountain ⛰️</b> or a <b>volcano 🌋</b>.<br>
🔵 Icon represents - Elevation of Mountain/Volcano from ground level is above <i>6000m</i><br>
🔴 Icon represents - Elevation of Mountain/Volcano from ground level is between <i>4000m</i> and <i>6000m</i><br>
🟠 Icon represents - Elevation of Mountain/Volcano from ground level is between <i>2000m</i> and <i>4000m</i><br>
🟢 Icon represents - Elevation of Mountain/Volcano from ground level is below <i>2000m</i><br>

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)

## Libraries Used 📋:

<li><b><i>Folium</i></b> - For Creating Map</li>
<li><b><i>Pandas</i></b> - To Read Data</li><br>

## How To Use 🖥️:


- Clone this repository<br>
`git clone https://github.com/ParagD25/mountain_&_volcano_mapping`

- Go into the repository<br>
`cd mountain_&_volcano_mapping`

- Remove current origin repository<br>
`git remote remove origin`
- Create new virtual python environment<br>
`python3 -m venv venv`
- Activate virtual python environment<br>
`source venv/bin/activate`
- Install all the libraries mentioned above
- Run Python file<br>
`python my_maps.py`
- Open the HTML File<br>
`Maps.html`

## Screenshots 📸:
<p><h3>Hovering over the map will show the name of respective mountain/volcano.</h3></p>

![hover_map](https://user-images.githubusercontent.com/77889567/123671550-0a84d380-d85c-11eb-98ee-d19946dd92a4.gif)

<p><h3>Can select between mountains and volcanoes or both.</h3></p>

![layer_map](https://user-images.githubusercontent.com/77889567/123671906-68192000-d85c-11eb-96de-38e2aa0841a6.gif)

<p align="center"><h3 align="center">Mountains can be classified as :</h3>
  <img src="https://github.com/ParagD25/Mapping/blob/master/images/img1.png" alt="Mountain" width="100%">
</p>

<p align="center"><h3 align="center">Volcanoes can be classified as :</h3>
  <img src="https://github.com/ParagD25/Mapping/blob/master/images/img2.png" alt="Volcano" width="100%">
</p>

## Contributing ©️:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
