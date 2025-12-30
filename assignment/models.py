from django.db import models
from django.utils.translation import gettext_lazy as _

class About(models.Model):
    about_heading = models.CharField(_("About"), max_length=50)
    about_description  = models.TextField(_("Description"), max_length=500)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"
    
    def __str__(self):
        return self.about_heading
    
    
class SocialLink(models.Model):
    platform = models.CharField(_("Platform"), max_length=25)
    social_link = models.URLField(_("Social Link"), max_length=200)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    class Meta:
        verbose_name = "SocialLink"
        verbose_name_plural = "Social Links"
    
    def __str__(self):
        return self.platform
    