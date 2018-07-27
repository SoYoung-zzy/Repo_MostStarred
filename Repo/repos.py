
import requests
import pygal

url = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
r = requests.get(url)
print("Status Code:",r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
names = []
#stars = []
plot_dicts = []
for repo_dic in repo_dicts:
    names.append(repo_dic['name'])
    #stars.append(repo_dic['stargazers_count'])
    if repo_dic['description']:
        plot_dict = {
            'value':repo_dic['stargazers_count'],
            'label':repo_dic['description'],
            'xlink':repo_dic['html_url'],
        }
        plot_dicts.append(plot_dict)
    else: continue

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.show_y_guides = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred C Projects on Github'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('C_repos.svg')
#chart.add('',stars)