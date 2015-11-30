from setuptools import setup

setup(
    name="electrum-creditbit-server",
    version="1.0",
    scripts=['run_electrum_creditbit_server.py','electrum-creditbit-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumcreditbitserver':'src'
        },
    py_modules=[
        'electrumcreditbitserver.__init__',
        'electrumcreditbitserver.utils',
        'electrumcreditbitserver.storage',
        'electrumcreditbitserver.deserialize',
        'electrumcreditbitserver.networks',
        'electrumcreditbitserver.blockchain_processor',
        'electrumcreditbitserver.server_processor',
        'electrumcreditbitserver.processor',
        'electrumcreditbitserver.version',
        'electrumcreditbitserver.ircthread',
        'electrumcreditbitserver.stratum_tcp',
        'electrumcreditbitserver.stratum_http'
    ],
    description="Creditbit Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="creditbit",
    maintainer_email="support@creditbit.org",
    license="GNU Affero GPLv3",
    url="https://github.com/creditbit/electrum-creditbit-server/",
    long_description="""Server for the Electrum Lightweight Creditbit Wallet"""
)


