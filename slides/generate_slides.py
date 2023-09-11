'''
this script reads in the output_ram.csv file
and populates a markdown template writing to slides.md
which can be used to generate slides using reveal.js
'''
import pandas as pd
import os
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment and load the templates
env = Environment(loader=FileSystemLoader('.'))
slide_project = env.get_template('slide_templates/template_project_horizontal.md')
slide_bullets = env.get_template('slide_templates/template_bullets_vertical.md')
slide_bullets2 = env.get_template('slide_templates/template_iframe_background.md')
slide_image = env.get_template('slide_templates/template_image.md')
slide_url = env.get_template('slide_templates/template_url_vertical.md')

# Read the title slide from title_template.md
with open('slide_templates/template_title.md', 'r') as title_file:
    markdown = title_file.read()

# Read data from CSV to pandas
df = pd.read_csv('output_ram.csv')
#group by project
df = df.groupby('Project')

# Add a slide for each project
for project in df['Project'].unique():
    # add project slide with description
    description = df.get_group(project[0])['Project description'].values[0]
    # make sure description is not nan
    if description != description:
        description = ''
    slide_content = slide_project.render(Project=project[0], Project_content=description)
    markdown += slide_content

    # check if value in Output type is RAM assessment:
    if 'RAM assessment' in df.get_group(project[0])['Output type'].values:
        # add slide template with image and use column "Output Media" as image_path
        image_path = df.get_group(project[0])['Output Media'].values[0]
        slide_content = slide_image.render(image_path=image_path)
        markdown += slide_content

    # add vertical slides with output bullets
    bullets = df.get_group(project[0])['Output description']
    #check if series contains NA
    if not bullets.isnull().values.any():
        slide_content = slide_bullets.render(Bullets=bullets.tolist())
        markdown += slide_content

    # add vertical slides with url
    url = df.get_group(project[0])['Landing page']
    if url.values[0] != '':
        slide_content = slide_url.render(URL=url.values[0])
        markdown += slide_content

    # add combined slide
    if (not bullets.isnull().values.any()) & (url.values[0] != ''):
        slide_content = slide_bullets2.render(bullet=bullets.tolist()[0], URL=url.values[0])
        markdown += slide_content
    
# Write the entire slide deck to a markdown file
with open('slides.md', 'w') as md_file:
    md_file.write(markdown)

print("Generated slides.md")
