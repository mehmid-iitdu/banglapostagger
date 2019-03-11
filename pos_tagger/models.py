from django.db import models


# Model of Sentence
class Sentences(models.Model):
    sentence = models.TextField()

    class Meta:
        verbose_name_plural = "Sentences"

    def __str__(self):
        return self.sentence


# Model of tag
class Tags(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    color = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        # template = '{0.name} {0.description}'
        return self.name


# Model of Sentence Tag table
class Sentence_Tag(models.Model):
    sentence = models.ForeignKey(Sentences, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Sentence_Tag"

    def __str__(self):
        template = '{0.sentence} {0.tag} {0.word}'
        return template.format(self)
