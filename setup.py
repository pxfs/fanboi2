from setuptools import setup, find_packages


setup(
    name="fanboi2",
    version="2018.11",
    description="Board engine behind fanboi.ch",
    long_description="",
    long_description_content_type="text/x-rst",
    url="https://github.com/forloopend/fanboi2",
    author="Kridsada Thanabulpong",
    author_email="sirn@ogsite.net",
    license="BSD-3-Clause",
    classifiers=[
        "Framework :: Pyramid",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet",
    ],
    keywords="web wsgi bfg pylons pyramid",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "alembic >=0.9, <0.10",
        "argon2_cffi",
        "celery >=4.1, <4.2",
        "dogpile.cache",
        "geoip2",
        "hiredis",
        "isodate",
        "MarkupSafe",
        "misaka",
        "passlib",
        "psycopg2",
        "pyramid >=1.9, <1.10",
        "pyramid_debugtoolbar",
        "pyramid_mako",
        "pyramid_nacl_session",
        "pyramid_services",
        "pyramid_tm",
        "python3-memcached",
        "pytz",
        "redis",
        "requests",
        "sqlalchemy >=1.2, <1.3",
        "transaction",
        "waitress",
        "wtforms >=2.1, <3.0",
        "zope.sqlalchemy",
    ],
    zip_safe=False,
    test_suite="fanboi2.tests",
    extras_require={
        "dev": ["honcho", "hupper", "pre-commit"],
        "test": ["nose", "coverage", "rednose"],
    },
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fbctl = fanboi2.cmd.ctl:main",
            "fbcelery = fanboi2.cmd.celery:main",
        ]
    },
)
