from setuptools import setup

setup(
    name="electrum-bitcore-server",
    version="1.0",
    scripts=['run_electrum_bitcore_server.py','electrum-bitcore-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumbitcoreserver':'src'
        },
    py_modules=[
        'electrumbitcoreserver.__init__',
        'electrumbitcoreserver.utils',
        'electrumbitcoreserver.storage',
        'electrumbitcoreserver.deserialize',
        'electrumbitcoreserver.networks',
        'electrumbitcoreserver.blockchain_processor',
        'electrumbitcoreserver.server_processor',
        'electrumbitcoreserver.processor',
        'electrumbitcoreserver.version',
        'electrumbitcoreserver.ircthread',
        'electrumbitcoreserver.stratum_tcp',
        'electrumbitcoreserver.stratum_http'
    ],
    description="Bitcore Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="bitcore",
    maintainer_email="support@bitcore.cc",
    license="GNU Affero GPLv3",
    url="https://github.com/bitcore/electrum-bitcore-server/",
    long_description="""Server for the Electrum Lightweight Bitcore Wallet"""
)


