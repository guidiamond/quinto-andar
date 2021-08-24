import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0


# The 6 lines of code below define the convolutional base using a common pattern: a stack of Conv2D and MaxPooling2D layers.
# As input, a CNN takes tensors of shape (image_height, image_width, color_channels), ignoring the batch size. If you are new to these dimensions, color_channels refers to (R,G,B). In this example, you will configure your CNN to process inputs of shape (32, 32, 3), which is the format of CIFAR images. You can do this by passing the argument input_shape to your first layer.
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
#
# # To complete the model, you will feed the last output tensor from the convolutional base (of shape (4, 4, 64)) into one or more Dense layers to perform classification. Dense layers take vectors as input (which are 1D), while the current output is a 3D tensor. First, you will flatten (or unroll) the 3D output to 1D, then add one or more Dense layers on top. CIFAR has 10 output classes, so you use a final Dense layer with 10 outputs.
model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10))

# Compile and train the model

# model = tf.keras.models.load_model(
#     "my_model.h5", custom_objects=None, compile=True, options=None
# )

try:
    with tf.device("GPU:0"):
        model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

        history = model.fit(
            train_images,
            train_labels,
            epochs=2,
            validation_data=(test_images, test_labels),
        )
        model.save("./quintoandar/my_model.h5")

        # plt.plot(history.history["accuracy"], label="accuracy")
        # plt.plot(history.history["val_accuracy"], label="val_accuracy")
        # plt.xlabel("Epoch")
        # plt.ylabel("Accuracy")
        # plt.ylim([0.5, 1])
        # plt.legend(loc="lower right")

        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
        print(f" loss: {test_loss}\n accuracy: {test_acc}")
except Exception as e:
    print(f"Error:\n {e}")
