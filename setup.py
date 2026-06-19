from setuptools import setup

setup(
    name="aur-shield",
    version="1.0.0",
    description="Превентивний сканер шкідливого коду для AUR пакетів перед їх встановленням",
    author="meow",
    scripts=["aur-shield"],
    data_files=[
        ('/etc/pacman.d/hooks', ['aur-hunter.hook'])
    ],
)
