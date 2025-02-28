import tensorflow as tf
# Load the .pb file
converter = tf.lite.TFLiteConverter.from_saved_model("X-TFLITE") # Change this to your directory with the saved_model.pb file
# Convert the model
tflite_model = converter.convert()
# Save the .tflite file
with open("X-TFLITE/X.tflite", "wb") as f: # Change this to where you want to save your .tflite model
   f.write(tflite_model)
