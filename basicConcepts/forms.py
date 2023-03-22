from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # Check if the file type is an image
            if not image.content_type.startswith('image'):
                raise forms.ValidationError('File is not an image')

            # Check if the file size is too large
            if image.size > 10 * 1024 * 1024: # 10MB
                raise forms.ValidationError('File size cannot exceed 10MB')

        return image
