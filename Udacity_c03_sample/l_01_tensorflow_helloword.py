import tensorflow as tf

# Create TensorFlow object called hello_constant
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
    print(output)
