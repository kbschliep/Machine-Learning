uhcs
ultrahigh carbon steel microstructure dataset and data visualization tools.

Zipped data directory sizes are listed as [compressed/uncompressed].

README.md                this text file.
download.sh		 shell script to download the complete dataset
setup.sh		 shell script to link data files into uhcsdb web application
uhcsdb/                  code for data visualization web application using representations computed with uhcs code
uhcsdata/                ultrahigh carbon steel dataset
  models.py		 python module defining sqlalchemy classes for accessing microstructures.sqlite from python
  microstructures.sqlite SQLite database containing microstructure and processing metadata
  micrographs/           microstructure image files; various image formats [258M/317M]
  representations/       Microstructure representations (HDF5 format) [1018M/1.5G]
  embed/                 Reduced-dimensionality microstructure representations (HDF5 format) [2.9M/33M]
  figures/               Reduced-dimensionality microstructure maps (png) [467M/503M]
tools/           	 Python scripts for computing reduced-dimensionality representations and maps
			 Shell scripts for populating the uhcsdb project directory with data from uhcsdata


To download the entire dataset into the structure shown in this README, simply download and run download.sh from materialsdata.nist.gov, assuming you have access to the curl and zip/unzip command line tools.