from setuptools import setup, find_packages

setup(name='NumPAL',
      version='1.1.0',
      description='An open',
      url='https://github.com/ait-protocol/NumPAL',
      author='LVH-Tony',
      author_email='tony.leviethung@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['langchain','langchain-core','pydantic','bittensor'],
      entry_points={}
)