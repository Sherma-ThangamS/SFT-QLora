from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name='sft_dpo_qlora',
    version='0.1.0',
    author='Sherma Thangam S',
    author_email='sshermathangam@gmail.com',
    description='SFT-DPO-QLora Trainer Package',
    long_description_content_type= 'text/x-rst`,
    long_description='A package that allows to train llm model in two methon SFT and DPO',
    url='https://github.com/Sherma-ThangamS/SFT-DPO-QLora',
    packages=find_packages(),
    install_requires=[
        'torch',
        'datasets',
        'peft',
        'transformers',
        'trl',
        'bitsandbytes', 
        'auto-gptq',
        'optimum',
        'einops'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='sft dpo qlora trainer',
    python_requires='>=3.9',
    entry_points={
    'console_scripts': [
        'sft_train=sft_dpo_qlora.trainerSFT:main',
        'dpo_train=sft_dpo_qlora.trainerDPO:main',
        ],
    },
)