# JSON_Input.py
# Created by: VIEC Team


class submodule_id:
    def __init__(self, id, device_address, config_type, measured_value, address, io_value):
        self.id = id
        self.device_address = device_address
        self.config_type = config_type
        self.measured_value = measured_value
        self.address = address
        self.io_value = io_value

class output_obj:
<<<<<<< HEAD
    def __init__(self, id, GPIO_pin, config_mode, high_input, low_input, high_output, low_output, divider, measured_value, io_value):
        self.id = id
        self.GPIO_pin = GPIO_pin
        self.config_mode = config_mode
        self.high_input = high_input
        self.low_input = low_input
        self.high_output = high_output
        self.low_output = low_output
        self.divider = divider
        self.measured_value = measured_value
        self.io_value = io_value
        self.input_index = 0
        
   # def newAttr(self, attr):
     #   setattr(self, attr, attr)
        
def input_submodule_objects(submodule_objects): #submodule_objects
    import json
    
#    with open("LIGHT_Input.json") as jsonFile:
#        submodule = json.load(jsonFile)
    submodule = bytes(submodule_objects)
    submodule = json.loads(submodule_objects)
=======
    def __init__(self, id, GPIO_pin, config_mode, tf_function, peak_voltage, io_value, measured_value):
        self.id = id
        self.GPIO_pin = GPIO_pin
        self.config_mode = config_mode
        self.tf_function = tf_function
        self.peak_voltage: peak_voltage
        self.io_value = io_value
        self.measured_value = measured_value


def input_submodule_objects(file):
    import json
    
    
    with open(file) as jsonFile:
        submodule = json.load(jsonFile)
>>>>>>> c4862df5f80c5f81d13362150356a2c45c5124a8

    submodule_objects = {submodule_object['id']: submodule_id(submodule_object['id'],
                                                              submodule_object['device_address'], submodule_object['config_type'],
                                                              submodule_object['measured_value'],
                                                              submodule_object['address'], submodule_object['io_value'])
                         for submodule_object in submodule}
    return submodule_objects


<<<<<<< HEAD
def output_submodule_objects(submodule_objects): #submodule_objects
  #  setattr(output_obj, "input_index", 0)
    import json
    
   # with open("LIGHT_Output.json") as jsonFile:
   #     submodule = json.load(jsonFile)

    submodule = bytes(submodule_objects)
    submodule = json.loads(submodule_objects)

    submodule_objects = {submodule_object['id']: output_obj(submodule_object['id'],
                                                              submodule_object['GPIO_pin'],
                                                              submodule_object['config_mode'], submodule_object['high_input'],
                                                              submodule_object['low_input'], submodule_object['high_output'],
                                                              submodule_object['low_output'], submodule_object['divider'],
                                                            submodule_object['measured_value'], submodule_object['io_value'])
=======
def output_submodule_objects(file):
    import json

    with open(file) as jsonFile:
        submodule = json.load(jsonFile)

    submodule_objects = {submodule_object['id']: submodule_id(submodule_object['id'],
                                                              submodule_object['GPIO_Pin'],
                                                              submodule_object['config_mode'],
                                                              submodule_object['tf_function'],
                                                              submodule_object['peak_voltage'], submodule_object['set_point'], submodule_object['measured_value'])
>>>>>>> c4862df5f80c5f81d13362150356a2c45c5124a8
                         for submodule_object in submodule}
    return submodule_objects
