from jinja2 import Template

def get_modern_template(data):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            :root {
                --accent-color: {{ data.customization.accent_color | default('#2563eb') }};
                --font-family: {{ data.customization.font_family | default('Arial, sans-serif') }};
                --font-size: {{ data.customization.font_size | default('14px') }};
                --line-spacing: {{ data.customization.line_spacing | default('1.5') }};
            }
            body {
                font-family: var(--font-family);
                font-size: var(--font-size);
                line-height: var(--line-spacing);
                color: #333;
                margin: {{ data.customization.page_margin | default('40px') }};
                background: white;
            }
            .header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 25px; border-bottom: 2px solid var(--accent-color); padding-bottom: 20px; }
            .header-text { flex: 1; }
            .profile-pic { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 2px solid var(--accent-color); margin-left: 20px; }
            h1 { font-size: 2.5em; margin: 0; color: #111; }
            h2 { color: var(--accent-color); border-bottom: 2px solid var(--accent-color); padding-bottom: 5px; margin-top: 25px; font-size: 1.4em; text-transform: uppercase;}
            h3 { margin-bottom: 0px; font-size: 1.1em; color: #111;}
            .contact-info { margin-bottom: 20px; font-size: 0.9em; color: #555; }
            .contact-info span { margin-right: 15px; }
            .summary { margin-bottom: 20px; }
            
            .section { margin-bottom: 20px; }
            
            .item { margin-bottom: 15px; }
            .item-header { display: flex; justify-content: space-between; align-items: baseline; }
            .item-title { font-weight: bold; }
            .item-subtitle { font-style: italic; color: #555; }
            .item-date { font-size: 0.9em; color: #777; }
            
            .skills-category { margin-bottom: 10px; }
            .skills-category strong { display: inline-block; width: 150px; color: #333; }
            
            ul { margin-top: 5px; padding-left: 20px; }
            li { margin-bottom: 5px; }
            
            a { color: inherit; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="header-text">
                <h1>{{ data.personal_info.name }}</h1>
                <div class="title">{{ data.personal_info.title }}</div>
                <div class="contact-info">
                    {% if data.personal_info.email %}<span>&#9993; {{ data.personal_info.email }}</span>{% endif %}
                    {% if data.personal_info.phone %}<span>&#9742; {{ data.personal_info.phone }}</span>{% endif %}
                    {% if data.personal_info.location %}<span>&#128205; {{ data.personal_info.location }}</span>{% endif %}
                    {% if data.personal_info.linkedin %}<span>&#128279; {{ data.personal_info.linkedin }}</span>{% endif %}
                    {% if data.personal_info.github %}<span>&#128279; {{ data.personal_info.github }}</span>{% endif %}
                    {% if data.personal_info.portfolio %}<span>&#128187; {{ data.personal_info.portfolio }}</span>{% endif %}
                </div>
            </div>
            {% if data.personal_info.profile_pic %}
            <div>
                <img src="{{ data.personal_info.profile_pic }}" class="profile-pic" alt="Profile Picture">
            </div>
            {% endif %}
        </div>

        {% if data.summary %}
        <div class="section summary">
            <h2>Professional Summary</h2>
            <p>{{ data.summary }}</p>
        </div>
        {% endif %}

        {% if data.experience %}
        <div class="section">
            <h2>Experience</h2>
            {% for exp in data.experience %}
            <div class="item">
                <div class="item-header">
                    <div class="item-title">{{ exp.role }}</div>
                    <div class="item-date">{{ exp.duration }}</div>
                </div>
                <div class="item-subtitle">{{ exp.company }}</div>
                <p style="margin-top:5px; white-space: pre-wrap;">{{ exp.description }}</p>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% if data.education %}
        <div class="section">
            <h2>Education</h2>
            {% for edu in data.education %}
            <div class="item">
                <div class="item-header">
                    <div class="item-title">{{ edu.degree }} in {{ edu.branch }}</div>
                    <div class="item-date">{{ edu.start_year }} - {{ edu.end_year }}</div>
                </div>
                <div class="item-subtitle">{{ edu.institute }} {% if edu.cgpa %}| CGPA: {{ edu.cgpa }}{% endif %}</div>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% if data.projects %}
        <div class="section">
            <h2>Projects</h2>
            {% for proj in data.projects %}
            <div class="item">
                <div class="item-header">
                    <div class="item-title">{{ proj.name }}</div>
                    <div class="item-date">
                        {% if proj.github %}<a href="{{ proj.github }}">GitHub</a>{% endif %}
                        {% if proj.github and proj.demo %} | {% endif %}
                        {% if proj.demo %}<a href="{{ proj.demo }}">Demo</a>{% endif %}
                    </div>
                </div>
                <div class="item-subtitle">Technologies: {{ proj.technologies }}</div>
                <p style="margin-top:5px; white-space: pre-wrap;">{{ proj.description }}</p>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% if data.skills %}
        <div class="section">
            <h2>Skills</h2>
            {% for category in data.skills %}
            <div class="skills-category">
                <strong>{{ category.name }}</strong>: 
                {{ category['items'] | join(', ') }}
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% if data.certifications and data.customization.show_certifications %}
        <div class="section">
            <h2>Certifications</h2>
            <ul>
                {% for cert in data.certifications %}
                <li>{{ cert }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}

        {% if data.achievements and data.customization.show_achievements %}
        <div class="section">
            <h2>Achievements</h2>
            <ul>
                {% for ach in data.achievements %}
                <li>{{ ach }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
        
    </body>
    </html>
    """
    template = Template(html_template)
    return template.render(data=data)
