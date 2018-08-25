% include('header.tpl')
% if error:
  <p class="error">{{error}}</p>
% else:
<ul>
  % for url in urls:
    <li>{{url}}</li>
  % end
</ul>
% end

% include('footer.tpl')
