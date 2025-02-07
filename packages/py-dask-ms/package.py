# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDaskMs(PythonPackage):
    """Donfig"""

    homepage = "https://github.com/ratt-ru/dask-ms"
    pypi = "dask-ms/dask_ms-0.2.23.tar.gz"

    license("BSD-3")

    # newer versions require numpy 2.0, test later
    #  version("0.2.23", sha256="54450f7cc0c16a464d8aa79e0e5bdaa49f6494155096ce35f9bbe628b585987b")
    #  version("0.2.22", sha256="f425ae0454b81436d533dbcf3c18ec0fce6d5013503213ea269d175697a7f69b")


    version("0.2.21", sha256="09a3b5823d37cf61bca5a8b03726123ff16cc7c57332b647162ce7f408cd8c91")
    version("0.2.20", sha256="708389c078e908dedd23d823019776a9124b4f009ebea834f798e8a8a3a0e1c3")
    version("0.2.19", sha256="892712e68df7a4f98daf4f2a0be406baad3ca92d301d38a00fac1d53ee6ca7a2")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-poetry", type="build")

    depends_on("py-appdirs@1.4.4:", type=("build", "run"))
    depends_on("py-dask@2023.1.1:2024.10 +array", type=("build", "run"))
    depends_on("py-donfig@0.8:", type=("build", "run"))
    depends_on("py-casacore@3.5.1:", type=("build", "run"))
    depends_on("py-numpy@:1.99", type=("build", "run"))
    depends_on("py-zarr@2.12:", type=("build", "run"))
    depends_on("py-xarray@2023.1.0:", type=("build", "run"))
    depends_on("py-s3fs@2023.1.0:", type=("build", "run"))
    depends_on("py-minio@7.2.0:", type=("build", "run"))
    depends_on("py-pytest@7.1.3:", type=("build", "run"))
    depends_on("py-pandas@2.1.2:", type=("build", "run"))
    depends_on("py-katdal@0.22:", type=("build", "run"))
    depends_on("py-fsspec@2022.7.0:", type=("build", "run"))
