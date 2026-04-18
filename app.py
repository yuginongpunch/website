from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


posts = []

post_id_counter = 1

@app.route('/')
def index():
    
    return render_template('index.html', posts=posts)

@app.route('/write', methods=['GET', 'POST'])
def write():
    global post_id_counter
    if request.method == 'POST':
        
        title = request.form.get('title')
        content = request.form.get('content')
        
        
        post = {
            'id': post_id_counter,
            'title': title,
            'content': content
        }
        posts.append(post)
        post_id_counter += 1
        return redirect(url_for('index'))
    
    
    return render_template('write.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if request.method == 'POST':
        
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')
        return redirect(url_for('index'))
    
    return render_template('edit.html', post=post)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    global posts
    
    posts = [p for p in posts if p['id'] != post_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
