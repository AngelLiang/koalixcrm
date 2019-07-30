from setuptools import setup, find_packages
from koalixcrm.version import KOALIXCRM_VERSION

setup(name='koalix-crm',
      version=KOALIXCRM_VERSION,
      description='koalixcrm is a tiny and easy to use Customer-Relationship-Management'
                  ' Software (CRM) including tiny and easy to use Accounting Software',
      url='http://github.com/scaphilo/koalixcrm',
      author='Aaron Riedener',
      author_email='aaron.riedener@gmail.com',
      license='BSD',
      packages=find_packages(exclude=["projectsettings", "documentation"]),
      install_requires=['Django==2.1.5',
                        'lxml>=3.8.0',
                        'olefile>=0.44',
                        'Pillow>=4.2.1',
                        'psycopg2-binary>=2.7.3',
                        'pytz==2017.2',
                        'django-grappelli==2.12.1',
                        'django-filebrowser==3.11.1',
                        'djangorestframework==3.9.4',
                        'markdown==2.6.11',
                        'django-filter==2.0.0',
                        'djangorestframework-xml==1.4.0',
                        'pandas==0.23.4',
                        'matplotlib==3.0.1'
                        ],
      zip_safe=False,
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 3.4', ],
      python_requires='~=3.5',
      include_package_data=True,
)
