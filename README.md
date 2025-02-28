# Converting Darknet models into tflite models for FPGA

Converting and evaluating the tflite model

Contact if need assistance: Joey; jmule2@umbc.edu

Note: Change any directories, file paths, and file names needed within the code to suit your needs
Step 1:
Run ‘convert.py’ with the following command/arguments
```
python3 convert.py -f your_config_file.cfg your_weights.weights your_output_folder
```

‘your_output_folder’ is where your converted tensorflow model will be saved (.pb file)

Step 2:

Run ‘convert_tflite.py’ to convert your .pb to a .tflite model
```
python3 convert_tflite.py
```
Step 3:

Run ‘time_eval_tflite.py’
```
python3 time_eval_tflite.py
```
If you see this when trying to gather inference time with the converted .tflite model:

RuntimeError: failed to invoke XNNPACK runtimeNode number X (TfLiteXNNPackDelegate) failed to invoke.


Reinstall python packages:
```
pip install "numpy<2" --force-reinstall

pip install --force-reinstall "scipy<1.12"

pip uninstall tensorflow -y
pip install tensorflow==2.13.0
```


Other common errors/issues

Shape error:

Sometimes if there is spacing within the .cfg file, and the ‘convert.py’ file has trouble extracting the input size.

Example:
```
[net]
                   <--- Here there is a space
batch=100
subdivisions=1
width=416
height=416
channels=3
momentum=0.949
decay=0.0005
angle=0
saturation = 1.5
exposure = 1.5
hue=.1
```

You need to make sure there is no space between [net] and the other information, such that the script can extract  the width and height values properly.
```
[net]
width=x
height=x
```

