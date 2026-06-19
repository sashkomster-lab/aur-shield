# Maintainer: sashkomster-lab <sashkomster@gmail.com>

pkgname=aur-shield
pkgver=1.0.0
pkgrel=1
pkgdesc="Preventive malware and IoC scanner for AUR packages before installation"
arch=('any')
url="https://github.com/sashkomster-lab/aur-shield"
license=('MIT')
depends=('python' 'pacman' 'zstd')
makedepends=('git')
source=("git+${url}.git")
sha256sums=('SKIP')

package() {
    # Navigate to the cloned repository directory safely
    cd "${srcdir}/${pkgname}"

    # Create necessary system directories inside the package root
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/etc/pacman.d/hooks"
    install -d "${pkgdir}/etc/aur-shield"

    # Install the executable script
    install -m 755 aur-shield "${pkgdir}/usr/bin/aur-shield"

    # Install the Alpm/Pacman hook
    install -m 644 aur-hunter.hook "${pkgdir}/etc/pacman.d/hooks/aur-hunter.hook"

    # Install the signature database
    install -m 644 signatures.txt "${pkgdir}/etc/aur-shield/signatures.txt"
}
