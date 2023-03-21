#!/usr/bin/env python3
import argparse
from os import makedirs, path
from shutil import rmtree, copytree
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader("plebian-website"),
    autoescape=select_autoescape()
)


boards = {
    'q64a': {
        'image_name': 'plebian-debian-bookworm-quartz64a.img.xz',
        'board_name': 'Quartz64 Model A',
    },
    'q64b': {
        'image_name': 'plebian-debian-bookworm-quartz64b.img.xz',
        'board_name': 'Quartz64 Model B',
    },
    'soquartz-blade': {
        'image_name': 'plebian-debian-bookworm-soquartz-blade.img.xz',
        'board_name': 'SOQuartz On Blade Baseboard'
    },
    'soquartz-cm4io': {
        'image_name': 'plebian-debian-bookworm-soquartz-cm4.img.xz',
        'board_name': 'SOQuartz On CM4IO Baseboard'
    },
    'soquartz-model-a': {
        'image_name': 'plebian-debian-bookworm-soquartz-model-a.img.xz',
        'board_name': 'SOQuartz On "Model A" Baseboard'
    },
}


def flashing_pages():
    d = {}
    for slug, board in boards.items():
        d[f"flashing-{slug}"] = {
            'template': 'os-choice.html',
            'target': f'/flashing/{slug}/',
            'extra_args': board
        }
        for os in ['windows', 'linux', 'macos']:
            d[f'flashing-{slug}-{os}'] = {
                'template': f'flashing-{os}.html',
                'target': f'/flashing/{slug}/{os}/',
                'extra_args': {**board, 'operating_system': os}
            }
    return d


base_url = '/'


pages = {
    'index': {
        'template': 'index.html',
        'target': '/',
        'title': '',
    },
    'about': {
        'template': 'about.html',
        'target': '/about/',
        'title': 'About',
    },
    'flashing': {
        'template': 'flashing.html',
        'target': '/flashing/',
        'title': 'Flashing',
        'extra_args': {
            'boards': boards
        }
    },
    'running': {
        'template': 'running.html',
        'target': '/running/',
        'title': 'Running',
    },
    'running-first-boot': {
        'template': 'running-first-boot.html',
        'target': '/running/first-boot/',
        'title': 'First Boot',
    },
    'running-software-choices': {
        'template': 'running-software-choices.html',
        'target': '/running/software-choices/',
        'title': 'Software Choices',
    },
    'running-updating': {
        'template': 'running-updating.html',
        'target': '/running/updating/',
        'title': 'Updating',
    },
    'running-dt-overlays': {
        'template': 'running-dt-overlays.html',
        'target': '/running/dt-overlays/',
        'title': 'Device Tree Overlays',
    },
}

pages.update(flashing_pages())


navigation = {
    'entries': [
        {
            'target': pages['index']['target'],
            'label': 'Plebian',
        },
        {
            'target': pages['about']['target'],
            'label': 'About',
        },
        {
            'target': pages['flashing']['target'],
            'label': 'Flashing'
        },
        {
            'target': pages['running']['target'],
            'label': 'Running'
        },
        {
            'target': 'https://github.com/Plebian-Linux/quartz64-images/',
            'label': 'Contribute',
        },
    ],
}


def copy_static_files(outdir):
    static_path = "plebian-website/static"
    copytree(static_path, outdir, dirs_exist_ok=True)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Plebian's Website")
    parser.add_argument("-o", "--outdir", default="build/")
    args = parser.parse_args()

    if path.exists(args.outdir):
        rmtree(args.outdir)
    makedirs(args.outdir)

    copy_static_files(args.outdir)

    for p_name, p in pages.items():
        template = env.get_template(p['template'])
        target_path = p['target'].lstrip('/')
        page_out = path.join(args.outdir, target_path)
        makedirs(page_out, exist_ok=True)
        extra_args = p.get('extra_args', {})
        with open(path.join(page_out, 'index.html'), 'w') as f:
            f.write(template.render(navigation=navigation, page=p,
                                    base_url=base_url, **extra_args))


if __name__ == '__main__':
    main()
