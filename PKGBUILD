# Maintainer: meow <meow@meow-omenl>
pkgname=aur-shield
pkgver=1.0.0
pkgrel=1
pkgdesc="Preventive malware and IoC scanner for AUR packages before installation"
arch=('any')
url="https://github.com/ТВІЙ_НІК_НА_GITHUB/aur-shield"
license=('MIT')
depends=('python' 'pacman' 'zstd')
makedepends=('python-setuptools')
source=("git+$url.git")
sha256sums=('SKIP')

package() {
  cd "$srcdir/$pkgname"
  python setup.py install --root="$pkgdir/" --optimize=1
}
