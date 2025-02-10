# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNumpyro(PythonPackage):
    """Numpyro"""

    homepage = "https://github.com/pyro-ppl/numpyro"
    pypi = "numpyro/numpyro-0.17.0.tar.gz"

    license("Apache-2.0")

    version("0.17.0", sha256="b4ad89e3bea8280980bbae3f712bf218314869db24cd1a2e07d90cee2f85b143")
    version("0.16.1", sha256="553ea56c729bdeb83d6eb6d455911113dc75f5eb25a59e3af31a7726313eee38")
    version("0.16.0", sha256="9e68c26332752cc950caa91ac084c9c9bea2f60982b6dfca6acb14247540e681")
    version("0.15.3", sha256="f445eeae6200f883d790d65ce29ff245f7a9639bac3322d993eccf91c44023b3")

    depends_on("py-setuptools", type="build")

    depends_on("py-jax", type=("build", "run"))
    depends_on("py-jaxlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-multipledispatch", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
