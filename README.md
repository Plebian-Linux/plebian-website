# Plebian's Website

This repository contains the code to generate the static plebian.org website.


## Setup

Either create a virtualenv and install the requirements through pip, or install
Jinja2 and Pygments from your package manager, the choice is yours.


## Building The Website

Run `./plebgen.py`, the output will be in `build/`.


## Testing The Website

It's a static website, so any webserver is able to serve it. However, for a
quick and lazy "does this work?" test, you can use
`python -m http.server --directory build/ 9000`.


## Contributing

Follow PEP8. (Use `pycodestyle` to check!)


## License

Unless stated otherwise, the contents of this repository are licensed as
follows:

 * `plebgen.py` is licensed under the GNU General Public License v3, the text
   the text of which can be found in the `LICENSE_GPL` file.
 * The templates, including the texts therein, as well as the static assets, are
   licensed under the Creative Commons Attribution-ShareAlike 4.0 International
   (CC BY-SA 4.0) License, the text of which can be found [on the creative
   commons website](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
