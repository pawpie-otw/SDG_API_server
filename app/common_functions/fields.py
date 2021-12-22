available_field = [{
    "name": "gender",
    "description": "Gender. \n Chance for male ~ 49%, for female ~51% (base on population statistics in Poland). \n type: string/text",
    "options":[
        {
            "name": "Equal",
            "description": "Equal chance for every gender",
            "input_type": "checkbox",
            "return_type": "bool"
        }
    ]
},
{
    "name": "first name",
    "description": "Polish first names fit to gender. \n type: string/text",
    "options":[
        {
            "name": "num_of_fnames",
            "description": "Number of first names",
            "input_type": "select",
            "default": 1,
            "options": [1,2,3],
            "return_type": "bool",
            "dependecy":{
                "field":"unregular_num_of_fnames",
                1: "blocked",
                2: "unblocked",
                3: "blocked"
                }
        },
        {
            "name": "unregular_num_of_fnames",
            "description": "Unregular number of first names",
            "input_type": "checkbox",
            "return_type": "bool",
        }
    ]
}]