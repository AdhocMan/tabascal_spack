# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKatdal(PythonPackage):
    """Donfig"""

    homepage = "https://github.com/ska-sa/katdal"
    pypi = "katdal/katdal-0.23.tar.gz"

    license("BSD")

    version("0.23", sha256="c99ae75fc36b2f199db9cff66d8e7a5fcaa1e4ffbf5706157a5d9f2046825f3f")
    version("0.22", sha256="1cd10b39023b1bfa6773e0940850bffa77aeb3633c936c1354468292c14fee21")
    version("0.21", sha256="a25613508a99eaf62ff73b0d8c7d2e80babb7879da828fe1d281c4f2c8c818eb")
    version("0.20.1", sha256="2d4fad417c51f6fef4b4a58fb5e2cb3b901a532aa884d536be7687a17b4f9655")
    version("0.20", sha256="52833244dafd6e7311dd1f846d654b58dae42ca46ce4453dcac3cfa5840ae4d1")
    version("0.19", sha256="e8abc7ef77de668353e6544651928dfd2ead25d73821b0539dac30c7e565c70e")

    depends_on("py-katversion", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
