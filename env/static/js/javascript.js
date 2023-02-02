$.getJSON('/data', function(data) {
  var $table = $('<table>');
  var $thead = $('<thead>');
  var $tbody = $('<tbody>');
  var $th = $('<th>');
  var $tr = $('<tr>');
  var $td = $('<td>');

  $th.append("Key");
  $th.append("Value");
  $thead.append($tr.append($th));
  $table.append($thead);

  for (var key in data) {
      var $tr = $('<tr>');
      var $td = $('<td>');
      $td.append(key);
      $td.append(data[key]);
      $tr.append($td);
      $tbody.append($tr);
  }
  $table.append($tbody);
  $('#table-container').append($table);
});