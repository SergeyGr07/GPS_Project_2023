let userCounter = 0;
tablebody = document.getElementById("tablebody");

const randomName = () => {
	const array = ["Mark", "Jacob", "Larry"];
	return array[Math.floor(Math.random() * array.length)];
};

const randomSurname = () => {
	const array = ["Otto", "Thornton", "The Bird"];
	return array[Math.floor(Math.random() * array.length)];
};

const randomUsername = () => {
	const array = ["@mdo", "@fat", "@twitter"];
	return array[Math.floor(Math.random() * array.length)];
};

const addData = () => {
	userCounter += 1;
	let tr = document.createElement("tr");
	tr.setAttribute("id", `${userCounter}`);
	tr.innerHTML = `
		<th scope="row">${userCounter}</th>
		<td>${randomName()}</td>
		<td>${randomSurname()}</td>
		<td>${randomUsername()}</td>
		<td class="text-center">
			<button onClick="removeData(${userCounter})" class="btn btn-outline-danger">🗑</button>
		</td>
	`;
	tablebody.append(tr);
};

const removeData = (id) => {
	//userCounter -= 1;
	removalObject = document.getElementById(id);
	removalObject.remove();
};

const removeAllData = () => {
	removalObject = document.getElementsByTagName("tr");
	while (removalObject.length > 1) {
		removalObject[1].remove();
	}
	userCounter = 0;
};
