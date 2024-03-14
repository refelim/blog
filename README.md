# blog
---
## 기능
### 1. main
   - username 표시
   - 회원가입, 로그인, 로그아웃, 블로그 들어가기 링크
### 2. blog
   - 게시글 작성
     - 로그인을 한 유저만 해당 기능 사용
     - 제목과 내용 작성가능
   - 게시글 목록 기능
     - 게시물의 제목,내용,게시물 번호,태그,작성자,확인 가능
     - 태그를 통한 검색, 게시글 작성, 메인 페이지 링크
   - 게시글 상세보기 기능
     - 제목 및 내용을 보는 기능
     - 게시글 순번을 통해 접속
   - 게시글 검색 기능
     - 태그에 따라 검색 가능
     - 검색한 게시물은 시간순에 따라 정렬이 가능
   - 게시글 수정 기능
     - 로그인을 한 유저만 접속가능
     - 본인의 게시글이 아니라면 수정이 불가
     - 제목 또는 내용을 수정하는 기능
   - 게시글 삭제 기능
     - 로그인을 한 유저만 접속가능
     - 본인의 게시글이 아니라면 수정이 불가
     - 게시글을 삭제 하는 기능
     - 삭제를 완료한 이후에 게시글 목록 화면으로 돌아감
     - 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능
### 3. users
   - 회원가입
     - 회원가입 기능
     - username, password, 프로필 사진 입력
   - 로그인 기능
     - 로그인 기능
     - username, password 입력
---
## 개발 환경
### - 사용 툴
  - VSCode
### - 사용 언어
  - HTML, JS
  - Python
### - Web Framework
  - Django
### - 서비스 배포
  - AWS(미구현)
---
## URL 구조
### - App main

|URL|Views Function|HTML FILE NAME|NOTE|
|------|---|---|---|
|''|main|main.html|index|

### - App blog

|URL|Views Function|HTML FILE NAME|NOTE|
|------|---|---|---|
|'blog/'|post_list|blog/post_list.html|게시글 목록|
|'blog/<<int:pk>>'|post_detail|blog/post_detail.html|게시글 세부사항|
|'blog/write'|post_write|blog/post_write.html|게시글 작성|
|'blog/delete/<<int:pk>>'|post_delete|blog/post_delete.html|게시글 삭제|
|'blog/edit/<<int:pk>>'|post_edit|blog/post_edit.html|게시글 수정|
|'blog/search/<<str:tags>>'|post_search|blog/post_search.html|태그를 통한 게시글 검색|

### - App users

|URL|Views Function|HTML FILE NAME|NOTE|
|------|---|---|---|
|users/login|login_view|users/login.html|로그인|
|users/logout|logout_view|x|로그아웃|
|users/register|register|users/register.html|회원가입|

---
## 트러블 슈팅

1. templatesError
   ```
   return render(request, "/users/register.html", context)
   ```
   templeates, urls, views 다 문제 없었지만, 연결 html 경로 제일 앞에 / 있어서 templatesError가 계속 나왔음
   
2.  태그가 DB에 들어왔지만, tag가 계속 None으로 보이는 상황
   ```
   # {% for post in posts %} 
            <li>번호 : {{ forloop.counter }} # {{post.tags}}
                <h1>제목 : <a href ="/blog/{{ post.id }}/">{{ post.title }}</a></h1>      
   ```
   ->
   ```
    # {% for tag in posts.tags.all %} 
    {{ tag.name }}
       {% if not forloop.last %}, {% endif %}
    {% endfor %}
   ```

