# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMinio(PythonPackage):
    """MinIO Python SDK is Simple Storage Service (aka S3) client to perform bucket
    and object operations to any Amazon S3 compatible object storage service."""

    homepage = "https://github.com/minio/minio-py"
    pypi = "minio/minio-7.1.2.tar.gz"

    license("Apache-2.0")

    version("7.2.4", sha256="d504d8464e5198fb74dd9b572cc88b185ae7997c17705e8c09f3fef2f439d984")
    version("7.2.3", sha256="4971dfb1a71eeefd38e1ce2dc7edc4e6eb0f07f1c1d6d70c15457e3280cfc4b9")
    version("7.2.2", sha256="7ed4e08825fdd395dbc934f5178a41b0db04afeaa54504728d2e6621791ab96b")
    version("7.2.1", sha256="d195fd6cc09a403635534215aaf231f0e2b82ac072444a39a7bc3f0ea6a4ba91")
    version("7.2.0", sha256="4b015b018d10c1505f7c3e724fa7c2267760ac7bee6463a624cbf22cd272877b")
    version("7.1.17", sha256="b0b687c1ec9be422a1f8b04c65fb8e43a1c090f9508178db57c434a17341c404")
    version("7.1.16", sha256="56ecb1e7e0103d2dc212fb460fdb70ab2abb7fa5685db378429325d96d95587a")
    version("7.1.15", sha256="fcf8ac2cef310d5ddff2bef2c42f4e5a8bb546b87bca5bf8832135db054ca4e1")
    version("7.1.14", sha256="230faf1d0db1c3ce09aef86b0eb38e994a64769e34dad4b77febf59bc90d8ab0")
    version("7.1.13", sha256="8828615a20cde82df79c5a52005252ad29bb022cde25177a4a43952a04c3222c")
    version("7.1.12", sha256="63111fedf67e07c5a4c8948b3a4e5ecbb372b522ea562bfa4d484194ec6a2b99")
    version("7.1.11", sha256="12ac2d1d4fd3cea159d625847445e1bfceba3fbc2f4ab692c2d2bf716f82246c")
    version("7.1.10", sha256="4a2e1c0d41fb4c0936be544b73fbb1f4eb85d17002b232f101bc701b0b1203e2")
    version("7.1.9", sha256="a711f3e6961ef083c161cee79f42a01d73369fc9111ccf76a74fb8d58b41d00a")
    version("7.1.8", sha256="c3fe5448ca281c88fe58f0486a73e0df6cdb05e8dbf72eb79e570e71125c1686")
    version("7.1.7", sha256="191278a7f572080b9677891fa19801750a8de3a25b978de73551409413e64362")
    version("7.1.6", sha256="54a5e6eefcc958c88c493cf116ba86e52341efab88686163594f2e9410385124")
    version("7.1.5", sha256="f33bb3d2a1b790d6ffc7b981c3f38c4f404d61c46de3cbd087fbf9d36a5f05ea")
    version("7.1.4", sha256="cea0d0d6fd6cb1361d43e5007126bad5e5e4af2e781c3912aecae66ad46b4aed")
    version("7.1.3", sha256="af8be2077821612f622f625baafef0fd4c1b04691a2a90a40be484fc606f7dcd")
    version("7.1.2", sha256="40d0cdb4dba5d5610d6599ea740cf827102db5bfa71279fc220c3cf7305bedc1")

    depends_on("py-setuptools", type="build")
    depends_on("py-certifi", type=("build", "run"))
    depends_on("py-urllib3", type=("build", "run"))
