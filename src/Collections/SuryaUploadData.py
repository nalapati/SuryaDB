'''
Created on Oct 28, 2010

@author: surya
'''

from mongoengine import *

class SuryaUploadData(Document):
    # A unique ID for a device
    deviceId = StringField(max_length=128, required=True)
    
    # filename
    filename = StringField(required=True)
        
    # The working file we will adjust during processing
    file = FileField()     

    # The original file, since we may transform the data during processing
    origFile = FileField()
       
    # The data type / MIME type of the uploading file    
    datatype = StringField(max_length=128, required=True) 
        
    # The time that the server receives the uploading datetime.datetime instance
    serverDatetime = DateTimeField(required=True)
        
    # The time that the picture is taken (provided by client)    
    recordDatetime = DateTimeField(required=True)          
        
    # For future extension. For example, store a json object here    
    misc = StringField()     
        
    # GPS info    
    gpsLatLong = GeoPointField()
    gpsAltitude = FloatField()         
                
    # False if an uploading has been marked as invalid    
    # (edited by management interface only)    
    # (or because of unreasonable value detected by our codes)    
    validFlag = BooleanField()     
       
    # Explain why a record is invalid. Having value only if valid_flag = False    
    invalidReason = StringField(max_length=1024)     
            
    # For ground truth image, putting GT as a tag or something like it.    
    # This tag is for management purpose only. Comma Separated Only    
    tag = StringField(max_length=128)     
    
    # Version    
    version = StringField(max_length=128)     
    
    # To support that 1 cell phone for multiple pumps.    
    auxId = StringField(max_length=128)
    
    # Deployment ID    
    deploymentId = StringField(max_length=128, required=True)
