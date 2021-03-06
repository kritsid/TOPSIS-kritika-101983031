from distutils.core import setup
setup(
  name = 'TOPSIS-kritika-101983031',         
  packages = ['TOPSIS-kritika-101983031'],   
  version = '0.8',
  license='MIT',
  description = 'This package allows you to implement topsis approach in python',
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'kritika aggarwal',                  
  author_email = 'kritikaaggarwal1621@gmail.com',      
  url = 'https://github.com/kritsid/TOPSIS-kritika-101983031', 
  download_url = 'https://github.com/kritsid/TOPSIS-kritika-101983031/archive/v_01.tar.gz',  
  keywords = ['TOPSIS'],   
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
