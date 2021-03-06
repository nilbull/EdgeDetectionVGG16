from PreprocessImage import *
from keras.models import load_model
import matplotlib.pyplot as plt

unet = load_model('unet-original.keras')

CustomImage = 'TOY.jpg'
plt.imshow(predict_custom_image(CustomImage, model=unet))