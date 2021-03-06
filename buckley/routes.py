from sketch import Route as r

routes = [  
  # admin area
  r(r'/admin/comments', 'buckley.admin.Comments'),
  r(r'/admin/cache_page/(.*)', 'buckley.admin.CacheView'),
  r(r'/admin/cache', 'buckley.admin.Cache'),
  r(r'/admin/pages', 'buckley.admin.Pages'),
  r(r'/admin/pages/<action>', 'buckley.admin.Pages'),
  r(r'/admin/pages/<action>/<key>', 'buckley.admin.Pages'),
  r(r'/admin/posts', 'buckley.admin.Posts'),
  r(r'/admin/posts/<action>', 'buckley.admin.Posts'),
  r(r'/admin/posts/<action>/<key>', 'buckley.admin.Posts'),
  r(r'/admin/status', 'buckley.admin.Statuses'),
  r(r'/admin/status/<action>', 'buckley.admin.Statuses'),
  r(r'/admin/status/<action>/<key>', 'buckley.admin.Statuses'),  
  r(r'/admin/settings', 'buckley.admin.Settings'),
  r(r'/admin<path:.*>', 'buckley.admin.Index', 'webwall-admin'),
  
  # API
  r(r'/data/status', 'buckley.controllers.StatusAPI'),
  
  # main blog
  r(r'/feed/microblog', 'buckley.controllers.MicroblogFeed', 'blog-feed'),
  r(r'/feed/<format:(rss|rss2|atom)>', 'buckley.controllers.Feed', 'blog-feed'),
  r(r'/feed', 'buckley.controllers.Feed', 'blog-feed'),
  r(r'/status', 'buckley.controllers.StatusIndex', 'status-index'),
  r(r'/status/<key>', 'buckley.controllers.StatusIndex', 'status-single'),
  r(r'/archive', 'buckley.controllers.Archive', 'blog-archive'),
  r(r'/archive/<page:\d+>', 'buckley.controllers.Archive', 'blog-archive'),
  r(r'/page/<page:\d+>', 'buckley.controllers.Index', 'blog-page'),
  r(r'/posts/<stub>', 'buckley.controllers.Post', 'blog-post'),
  r(r'/<stub>', 'buckley.controllers.Page', 'blog-page'),
  r(r'/', 'buckley.controllers.Index', 'blog-index'),
]