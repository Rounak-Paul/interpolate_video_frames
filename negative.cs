using System;
using System.Drawing;

namespace ImageProcessingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Load the original image
            var originalImage = Image.FromFile("C:\\Path\\To\\Image.jpg");

            // Create a new bitmap with the same dimensions as the original image
            var newImage = new Bitmap(originalImage.Width, originalImage.Height);

            // Loop through each pixel in the new image
            for (int x = 0; x < newImage.Width; x++)
            {
                for (int y = 0; y < newImage.Height; y++)
                {
                    // Get the color of the pixel in the original image at the current position
                    var originalColor = originalImage.GetPixel(x, y);

                    // Create a new color by inverting the RGB values of the original color
                    var newColor = Color.FromArgb(255 - originalColor.R,
                                                255 - originalColor.G,
                                                255 - originalColor.B);

                    // Set the pixel in the new image to the new color
                    newImage.SetPixel(x, y, newColor);
                }
            }

            // Save the new image to a file
            newImage.Save("C:\\Path\\To\\NewImage.jpg");
        }
    }
}
