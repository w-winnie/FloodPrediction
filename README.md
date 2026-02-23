## Set up environment from requirements.txt 

conda create --name floodPred python=3.10  
conda activate floodPred  

pip install -r requirements.txt  


## To recreate from environment.yml file  

conda env create -f environment.yml  


## Update environment files  

conda env export > environment.yml  
pip freeze > requirements.txt  


## NOTEBOOKS overview:  
sandbox_0_data_import.ipynb - Get data (gives options for both copernicus or GEE)  


## Some useful resources:   

### DATA:  
#### google earth engine  
https://earthengine.google.com/  
#### copernicus api  
https://emergency.copernicus.eu/data/   
https://dataspace.copernicus.eu/news/2023-9-28-accessing-sentinel-mission-data-new-copernicus-data-space-ecosystem-apis  
#### copernicus data space  
https://dataspace.copernicus.eu/  
https://github.com/cloudtostreet/Sen1Floods11   
   
 
#### OTHER MODELS:  
https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-1.0-100M-sen1floods11    
https://wbwaterdata.org/dataset/global-flood-monitoring-system-gfms   


