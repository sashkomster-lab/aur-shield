# Maintainer: sashkomster-lab
pkgname=aur-shield
pkgver=1.0.0
pkgrel=1
pkgdesc="Preventive malware and IoC scanner for AUR packages before installation"
arch=('any')
url="https://github.com/sashkomster-lab/aur-shield"
license=('MIT')
depends=('python' 'pacman' 'zstd')
source=("git+https://github.com/sashkomster-lab/aur-shield.git")
sha256sums=('SKIP')

package() {
    cd "${srcdir}/aur-shield"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/etc/pacman.d/hooks"
    install -d "${pkgdir}/etc/aur-shield"

    install -m 755 aur-shield "${pkgdir}/usr/bin/aur-shield"
    install -m 644 aur-hunter.hook "${pkgdir}/etc/pacman.d/hooks/aur-hunter.hook"
    install -m 644 signatures.txt "${pkgdir}/etc/aur-shield/signatures.txt"
}
