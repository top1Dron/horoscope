<!DOCTYPE html>
<html>
    <head>
		<meta charset='utf-8'>
		<title>Гороскоп на сегодня</title>
		<link rel="stylesheet"
			href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
			integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
			crossorigin="anonymous"/>
		<script
  			src="https://code.jquery.com/jquery-3.4.1.min.js"
  			integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
  			crossorigin="anonymous">
		</script>
	</head>
    <body>
		<div class="container" id="date">
			<h1>Что день {{date}} готовит</h1>
			%if specialDate > 0.5:
			<h2>Сегодня особенный день!</h2>
			%end
			<div class="row" id='container'>
			% number = 0
			% for prophecy in prophecies:
				<div class="col-4" id="paragraph-{{number}}">
					<p>{{prophecy}}</p>
				</div>
				%number +=1
			%end
			</div>
			
			<a href='/about'>О реализации</a>
		</div>
	</body>
	<script text="javascript">
		console.log({{specialDate}})
	</script>
	<script src="/static/scripts/script.js"></script>
</html>