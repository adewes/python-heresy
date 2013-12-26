repetitions = 10

people = []

for i in range(0,500):
    person = {'first_name' : 'Andreas %d' % i,'last_name' : 'Dewes %d' % i,'email' : 'andreasdewes@gmx%d.de' % i}
    people.append(person)

context = {'people' : people}

heresy = {
    'context' : context,
    'template_name' : 'test.html',
    'templates' : {
    'test.html' : """
    <table>
        <% for person in people: %>
        <tr>
            <%= include('_person.html',**person) %>
        </tr>
        <% end %>
    </table>
    """,
    '_person.html' : """
    <tr>
        <td><%=h first_name %></td>
        <td><%=h last_name %></td>
        <td><%=h email %></td>
    </tr>
    """}
}

jinja2 = {
    'context' : context,
    'template_name' : 'test.html',
    'templates' : {
    'test.html' : """
    <table>
        {% for person in people %}
        <tr>
            {% include "_person.html" with context %}
        </tr>
        {% endfor %}
    </table>
    """,
    '_person.html' : """
    <tr>
        <td>{{person.first_name|escape}}</td>
        <td>{{person.last_name|escape}}</td>
        <td>{{person.email|escape}}</td>
    </tr>
    """}
}

django = {
    'context' : context,
    'template_name' : 'test.html',
    'templates' : {
    'test.html' : """
    <table>
        {% for person in people %}
        <tr>
            {% include "_person.html" with person=person %}
        </tr>
        {% endfor %}
    </table>
    """,
    '_person.html' : """
    <tr>
        <td>{{person.first_name|escape}}</td>
        <td>{{person.last_name|escape}}</td>
        <td>{{person.email|escape}}</td>
    </tr>
    """}
}