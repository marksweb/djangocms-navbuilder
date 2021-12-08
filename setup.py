from setuptools import find_packages, setup

INSTALL_REQUIREMENTS = [
    "Django>=2.2,<4",
    "django-cms",
    "djangocms-attributes-field",
]


setup(
    name="djangocms-url-manager",
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description="django cms navigation plugin",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    install_requires=INSTALL_REQUIREMENTS,
    author="Mark Walker",
    author_email="theshow@gmail.com",
    url="http://github.com/marksweb/djangocms-navigation",
    license="BSD",
)
