# Plebian's Website

This repository contains the code to generate the static plebian.org website.


## Setup

Either create a virtualenv and install the requirements through pip, or install
Jinja2 from your package manager, the choice is yours.


## Building The Website

Run `./plebgen.py`, the output will be in `build/`.


## Testing The Website

It's a static website, so any webserver is able to serve it. However, for a
quick and lazy "does this work?" test, you can use
`python -m http.server --directory build/ 9000`.


## Contributing

Follow PEP8. (Use `pycodestyle` to check!)


## License

The contents of this repository have been published under the license found
in the `LICENSE` file of this repository, unless stated otherwise.
