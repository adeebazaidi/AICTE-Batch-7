from jinja2 import Template

def get_minimal_template(data):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            :root {
                --accent-color: {{ data.customization.accent_color | default('#000000') }};
                --font-family: {{ data.customization.font_family | default('Helvetica, sans-serif') }};
                --font-size: {{ data.customization.font_size | default('13px') }};
                --line-spacing: {{ data.customization.line_spacing | default('1.6') }};
            }
            body {
                font-family: var(--font-family);
                font-size: var(--font-size);
                line-height: var(--line-spacing);
                color: #222;
                margin: {{ data.customization.page_margin | default('50px') }};
                background: white;
            }
            h1 { font-size: 2.8em; font-weight: 300; letter-spacing: 2px; margin-bottom: 5px; color: var(--accent-color); }
            .title { font-size: 1.1em; color: #666; letter-spacing: 1px; margin-bottom: 25px; text-transform: uppercase; }
            
            .header-container { display: flex; justify-content: space-between; align-items: flex-start; }
            .header-text { flex: 1; }
            .profile-pic { width: 90px; height: 90px; border-radius: 5px; object-fit: cover; filter: grayscale(100%); margin-left: 20px; }
            
            .contact-info { display: flex; flex-wrap: wrap; gap: 20px; font-size: 0.9em; color: #555; margin-bottom: 40px; border-top: 1px solid #eee; border-bottom: 1px solid #eee; padding: 15px 0; }
            
            h2 { font-size: 1.2em; text-transform: uppercase; letter-spacing: 2px; margin-top: 35px; margin-bottom: 20px; color: var(--accent-color); font-weight: 600;}
            
            .item { margin-bottom: 25px; }
            .item-header { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid #f0f0f0; padding-bottom: 4px; margin-bottom: 8px; }
            .item-title { font-weight: 600; font-size: 1.1em; color: #111; }
            .item-date { font-size: 0.9em; color: #777; text-align: right; }
            .item-subtitle { font-style: italic; color: #555; margin-bottom: 8px; }
            
            p { margin-top: 0; }
            ul { margin-top: 0; padding-left: 15px; }
            li { margin-bottom: 5px; }
            
            .skills-grid { display: flex; flex-wrap: wrap; gap: 10px; }
            .skill-badge { background: #f4f4f4; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; border: 1px solid #eee; }
            
            a { color: inherit; text-decoration: none; }
        </style>
    </head>
    <body>
        <header>
            <div class="header-container">
                <div class="header-text">
                    <h1>{{ data.personal_info.name }}</h1>
                    <div class="title">{{ data.personal_info.title }}</div>
                </div>
                {% if data.personal_info.profile_pic %}
                <div>
                    <img src="{{ data.personal_info.profile_pic }}" class="profile-pic" alt="Profile Picture">
                </div>
                {% endif %}
            </div>
            <div class="contact-info">
                {% if data.personal_info.email %}<span>{{ data.personal_info.email }}</span>{% endif %}
                {% if data.personal_info.phone %}<span>{{ data.personal_info.phone }}</span>{% endif %}
                {% if data.personal_info.location %}<span>{{ data.personal_info.location }}</span>{% endif %}
                {% if data.personal_info.linkedin %}<span>{{ data.personal_info.linkedin }}</span>{% endif %}
                {% if data.personal_info.github %}<span>{{ data.personal_info.github }}</span>{% endif %}
                {% if data.personal_info.portfolio %}<span>{{ data.personal_info.portfolio }}</span>{% endif %}
            </div>
        </header>

        {% if data.summary %}
        <div class="section">
            <h2>Profile</h2>
            <div style="font-size: 1.05em; color: #444;">{{ data.summary }}</div>
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
                <p style="white-space: pre-wrap; font-size: 0.95em;">{{ exp.description }}</p>
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
                        {% if proj.github %}<a href="{{ proj.github }}" target="_blank" style="text-decoration: underline;">GitHub</a>{% endif %}
                        {% if proj.github and proj.demo %} | {% endif %}
                        {% if proj.demo %}<a href="{{ proj.demo }}" target="_blank" style="text-decoration: underline;">Live Demo</a>{% endif %}
                    </div>
                </div>
                <div class="item-subtitle">Tech: {{ proj.technologies }}</div>
                <p style="white-space: pre-wrap; font-size: 0.95em;">{{ proj.description }}</p>
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

        {% if data.skills %}
        <div class="section">
            <h2>Skills</h2>
            {% for category in data.skills %}
            <div style="margin-bottom: 15px;">
                <div style="margin-bottom: 8px; font-weight: bold; color: #555; text-transform: uppercase; font-size: 0.85em; letter-spacing: 1px;">{{ category.name }}</div>
                <div class="skills-grid">
                    {% for skill in category['items'] %}
                    <span class="skill-badge">{{ skill }}</span>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
        
    </body>
    </html>
    """
    template = Template(html_template)
    return template.render(data=data)
