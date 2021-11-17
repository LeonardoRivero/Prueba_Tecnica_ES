async function getAllCameras() {
  url = "/api/camera/list/"
  let response = await request_get(url);
  let allData = await response.json()
  return allData
  console.log(allData, "entro de una");
}
