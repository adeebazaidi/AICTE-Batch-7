from jinja2 import Template

def get_twocolumn_template(data):
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
                margin: 0;
                padding: 0;
                background: white;
            }
            .page {
                display: flex;
                min-height: 297mm;
                width: 100%;
            }
            .sidebar {
                width: 30%;
                background-color: var(--accent-color);
                color: white;
                padding: 40px 20px;
                box-sizing: border-box;
            }
            .main-content {
                width: 70%;
                padding: 40px;
                box-sizing: border-box;
            }
            h1 { font-size: 2.2em; margin-top: 0; margin-bottom: 10px; color: #111; }
            .title { font-size: 1.2em; color: var(--accent-color); margin-bottom: 30px; }
            
            h2 { font-size: 1.4em; border-bottom: 2px solid #ccc; padding-bottom: 5px; margin-top: 25px; color: #111; }
            .sidebar h2 { color: white; border-bottom: 1px solid rgba(255,255,255,0.3); margin-top: 30px; }
            
            .contact-item { margin-bottom: 10px; font-size: 0.9em; word-break: break-word; }
            
            .item { margin-bottom: 20px; }
            .item-header { display: flex; justify-content: space-between; align-items: baseline; }
            .item-title { font-weight: bold; font-size: 1.1em; color: #222; }
            .item-subtitle { font-style: italic; color: #555; }
            .item-date { font-size: 0.9em; color: var(--accent-color); font-weight: bold; }
            
            .skills-category { margin-bottom: 15px; }
            .skills-category strong { display: block; margin-bottom: 5px; }
            
            ul { margin-top: 5px; padding-left: 20px; }
            li { margin-bottom: 5px; }
            .sidebar ul { padding-left: 15px; }
            .sidebar li { margin-bottom: 8px; font-size: 0.95em; }
            
            .profile-pic { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 20px; border: 3px solid rgba(255,255,255,0.3); }
            a { color: inherit; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="page">
            <div class="sidebar">
            {% if data.personal_info.profile_pic %}
            <div style="text-align: center;">
                <img src="{{ data.personal_info.profile_pic }}" class="profile-pic" alt="Profile Picture">
            </div>
            {% endif %}
            <h2 style="margin-top: 0;">Contact</h2>
            {% if data.personal_info.email %}<div class="contact-item">&#9993; {{ data.personal_info.email }}</div>{% endif %}
            {% if data.personal_info.phone %}<div class="contact-item">&#9742; {{ data.personal_info.phone }}</div>{% endif %}
            {% if data.personal_info.location %}<div class="contact-item">&#128205; {{ data.personal_info.location }}</div>{% endif %}
            {% if data.personal_info.linkedin %}<div class="contact-item">&#128279; {{ data.personal_info.linkedin }}</div>{% endif %}
            {% if data.personal_info.github %}<div class="contact-item">&#128279; {{ data.personal_info.github }}</div>{% endif %}
            {% if data.personal_info.portfolio %}<div class="contact-item">&#128187; {{ data.personal_info.portfolio }}</div>{% endif %}

            {% if data.skills %}
            <h2>Skills</h2>
            {% for category in data.skills %}
            <div class="skills-category">
                <strong>{{ category.name }}</strong>
                <div style="font-size: 0.9em; opacity: 0.9;">{{ category['items'] | join(', ') }}</div>
            </div>
            {% endfor %}
            {% endif %}
            
            {% if data.certifications and data.customization.show_certifications %}
            <h2>Certifications</h2>
            <ul>
                {% for cert in data.certifications %}
                <li>{{ cert }}</li>
                {% endfor %}
            </ul>
            {% endif %}

            {% if data.achievements and data.customization.show_achievements %}
            <h2>Achievements</h2>
            <ul>
                {% for ach in data.achievements %}
                <li>{{ ach }}</li>
                {% endfor %}
            </ul>
            {% endif %}
        </div>
        
        <div class="main-content">
            <h1>{{ data.personal_info.name }}</h1>
            <div class="title">{{ data.personal_info.title }}</div>

            {% if data.summary %}
            <div class="section">
                <h2 style="margin-top: 0;">Professional Summary</h2>
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
                    <p style="margin-top:8px; white-space: pre-wrap; font-size: 0.95em;">{{ exp.description }}</p>
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
                    <div class="item-subtitle">Tech: {{ proj.technologies }}</div>
                    <p style="margin-top:8px; white-space: pre-wrap; font-size: 0.95em;">{{ proj.description }}</p>
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
        </div>
        </div>
    </body>
    </html>
    """
    template = Template(html_template)
    return template.render(data=data)
